// Fill out your copyright notice in the Description page of Project Settings.


#include "Lamp.h"

// Sets default values
ALamp::ALamp()
{
 	// Set this actor to call Tick() every frame.  You can turn this off to improve performance if you don't need it.
	PrimaryActorTick.bCanEverTick = true;
    LampMesh = CreateDefaultSubobject<UStaticMeshComponent>(TEXT("Lamp"));

}

// Called when the game starts or when spawned
void ALamp::BeginPlay()
{
	Super::BeginPlay();
    //Crea el mesh de la lampara
    
   
    

    Init();
}

// Called every frame
void ALamp::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);
   

   
}
void ALamp::LightOn() {

    FOnTimelineFloat progressFunction{};
    int index = 0;
    for (ULightComponent* TemporalLight : LightsLamp)
    {
        TemporalLight->SetIntensity(InicialIntesitys[index]);
        index++;
    }
    if (InstanceMaterial != nullptr)
    {
        InstanceMaterial->SetScalarParameterValue(emissionParamName, emissionIntensity);
        LampMesh->SetMaterial(IndexOfMaterial, InstanceMaterial);
    }
    else {
        UE_LOG(LogTemp, Warning, L"null");
    }

    //Enciden basado en curve
   // CurveOn->GetFloatValue(DeltaSeconds)
   /*
    progressFunction.BindUFunction(this, "InterpolateIntensity");
    MyTimline.AddInterpFloat(CurveOn, progressFunction, FName{ TEXT("BlendIntensity") });
    MyTimline.PlayFromStart();*/
}
void ALamp::InterpolateIntensity(float FValue)
{
    float StartIntesity = 0.0f;
    float FinalIntesity = 1.0f;
    float LastIntesity = 0.0f;
    
    LastIntesity = FMath::Lerp(StartIntesity, FinalIntesity, FValue);
    if (InstanceMaterial != nullptr)
    {
        InstanceMaterial->SetScalarParameterValue(emissionParamName, LastIntesity);
        LampMesh->SetMaterial(IndexOfMaterial, InstanceMaterial);
    }
    else {
        UE_LOG(LogTemp, Warning, L"null");
    }

  
}

void ALamp::LightOff() {

    for (ULightComponent* TemporalLight : LightsLamp)
    {
        TemporalLight->SetIntensity(0.0f);
    }
    if (InstanceMaterial != nullptr)
    {
        InstanceMaterial->SetScalarParameterValue(emissionParamName, 0);
        LampMesh->SetMaterial(IndexOfMaterial, InstanceMaterial);
    }
    else {
        UE_LOG(LogTemp, Warning, L"null");
    }
 
}
void ALamp::Flirck() {

}
void ALamp::Init() {
    //Configuracion inicial
    //Almacena todas las luces
    //Almacena sus valores inciales de intesity
   
 
 TArray<UActorComponent*> TemporalComponents;
 this->GetComponents(ULightComponent::StaticClass(), TemporalComponents, false);

        for (UActorComponent* TemporalLight : TemporalComponents)
            {
            ULightComponent* light = Cast<ULightComponent>(TemporalLight);
             LightsLamp.Add(light);
             InicialIntesitys.Add(light->Intensity);
             UE_LOG(LogTemp, Log, TEXT("Found UObject named: %s"), *light->GetName());
         }

        //Crea copia del material con emission    
        if (LampMesh != nullptr) {
          
            InstanceMaterial=  UMaterialInstanceDynamic::Create(LampMesh->GetMaterial(IndexOfMaterial), this);
           
        }
        else {
            UE_LOG(LogTemp, Warning, L"null");
        }
}

