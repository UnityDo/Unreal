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
	
}

// Called every frame
void ALamp::Tick(float DeltaTime)
{
	Super::Tick(DeltaTime);

}
void ALamp::LightOn() {
    for (ULightComponent* TemporalLight : LightsLamp)
    {
        TemporalLight->SetIntensity(GetLumenByType());
    }

}
void ALamp::LightOff() {

    for (ULightComponent* TemporalLight : LightsLamp)
    {
        TemporalLight->SetIntensity(0.0f);
    }
    

}
void ALamp::Flirck() {

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


