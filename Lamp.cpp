// Fill out your copyright notice in the Description page of Project Settings.


#include "Lamp.h"

// Sets default values
ALamp::ALamp()
{
 	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;
	IntensityOn= 3000.0f;
	lumensLamp = LumensType::Bulb450;
	LampMesh = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("Lamp"));

}

// Called when the game starts or when spawned
void ALamp::BeginPlay()
{
	Super::BeginPlay();

    //Configura el timeline
    if (OnCurve)
    {
        FOnTimelineFloat TimelineCallback;
        FOnTimelineEventStatic TimelineFinishedCallback;

        TimelineCallback.BindUFunction(this, FName("ExecuteTimeline"));
        TimelineFinishedCallback.BindUFunction(this, FName("OnFinishTimline"));

        MyTimeline = NewObject<UTimelineComponent>(this, FName("OnAnimation"));
        MyTimeline->AddInterpFloat(OnCurve, TimelineCallback);
        MyTimeline->SetTimelineFinishedFunc(TimelineFinishedCallback);
        MyTimeline->RegisterComponent();
    }
  
}

// Called every frame
void ALamp::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

    if (MyTimeline != NULL)
    {
        MyTimeline->TickComponent(DeltaTime, ELevelTick::LEVELTICK_TimeOnly, NULL);
    }

}
void ALamp::LightOn() {
    for (ULightComponent* TemporalLight : LightsLamp)
    {
        TemporalLight->SetIntensity(GetLumenByType());
    }

       
      
        DynMaterial->SetScalarParameterValue(ParamEmissionName, EmissionIntesity);
        DynMaterial->SetScalarParameterValue(ParamOpacity, OpacityIntesity);
    
        UE_LOG(LogTemp, Warning, TEXT("[%s] create Material name : %s emision %f"), *this->GetName(), *LampMesh->GetMaterial(0)->GetName(), EmissionIntesity);
    
        
}
void ALamp::LightOff() {

    for (ULightComponent* TemporalLight : LightsLamp)
    {
        TemporalLight->SetIntensity(0.0f);
    }
    
    DynMaterial->SetScalarParameterValue(ParamEmissionName, 0.0f);
    DynMaterial->SetScalarParameterValue(ParamOpacity, 0.0f);

}
void ALamp::Flirck() {

    //MyTimeline->PlayFromStart();
    MyTimeline->SetLooping(true);
    MyTimeline->Play();

}

float ALamp::GetLumenByType()
{
    float intesity = 0;
    switch (lumensLamp)
    {
    case LumensType::NoLumen:
        intesity = 0;
        break;
    case LumensType::Bulb450:
        intesity = 450;
        break;
    case LumensType::Bulb800:
        intesity = 800;
        break; 
    case LumensType::Bulb1100:
            intesity = 1100;
            break;
    case LumensType::Bulb1600:
                intesity = 1600;
                break;
    case LumensType::Bulb2600:
        intesity = 2600;
        break;

    case LumensType::Bulb5800:
        intesity = 5800;
        break;



    default: break;
    }


	return intesity;
}

void ALamp::ConfigurationLamp(float Emission, float Opacity)
{
    EmissionIntesity = Emission;
    OpacityIntesity = Opacity;
    DynMaterial = UMaterialInstanceDynamic::Create(LampMesh->GetMaterial(indexOfMaterial), this);
    LampMesh->SetMaterial(indexOfMaterial, DynMaterial);

    //Mete los lights en el array, no se puede obtener directamente 
    TArray<UActorComponent*> temporalArray= this-> GetComponentsByClass(ULightComponent::StaticClass());
   

    for (UActorComponent* component : temporalArray)
    {
        ULightComponent* lightComp = Cast<ULightComponent>(component);
        check(lightComp != nullptr);
        LightsLamp.Add(lightComp);
    }

}

void ALamp::ExecuteTimeline()
{

    TimelineValue = MyTimeline->GetPlaybackPosition();
    CurveValue= OnCurve->GetFloatValue(TimelineValue);
    UE_LOG(LogTemp, Warning, TEXT("Text %f"), CurveValue);

    for (ULightComponent* TemporalLight : LightsLamp)
    {
        TemporalLight->SetIntensity(CurveValue *100);
    }

    DynMaterial->SetScalarParameterValue(ParamEmissionName, CurveValue *100);
    DynMaterial->SetScalarParameterValue(ParamOpacity, 1);


}

void ALamp::OnFinishTimline()
{
    UE_LOG(LogTemp, Warning, TEXT("Acabado"));
}


