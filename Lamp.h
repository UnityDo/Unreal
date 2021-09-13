// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Containers/Array.h"
#include "Components/LightComponent.h"
#include "Components/TimelineComponent.h"
#include "Lamp.generated.h"



UCLASS()
class PENTAKILL_CHARACTER_API ALamp : public AActor
{
	GENERATED_BODY()
	
public:	
	// Sets default values for this actor's properties
	ALamp();
	UFUNCTION(BlueprintCallable, Category = "Control Lamp")
		void Init();
	UFUNCTION(BlueprintCallable, Category = "Control Lamp")
		void LightOn();
	void InterpolateIntensity(float FValue);
	UFUNCTION(BlueprintCallable, Category = "Control Lamp")
		void LightOff();
	UFUNCTION(BlueprintCallable, Category = "Control Lamp")
		void Flirck();

protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;
	UMaterialInstanceDynamic* InstanceMaterial;
	TArray<ULightComponent*> LightsLamp;
	TArray<float> InicialIntesitys;

private:
	float timeValue;
	float TimelineValue;
	FTimeline MyTimline;

public:	
	// Called every frame
	virtual void Tick(float DeltaTime) override;
	
	UPROPERTY(VisibleAnywhere)
		UStaticMeshComponent* LampMesh;
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Control Lamp")
		int32 IndexOfMaterial; 
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Control Lamp")
		float emissionIntensity;
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Control Lamp")
		FName emissionParamName;
	UPROPERTY(EditDefaultsOnly, Category = Curve)
		UCurveFloat* CurveOn;
	UPROPERTY(EditDefaultsOnly, Category = Curve)
		UCurveFloat* CurveOff;
	UPROPERTY(EditDefaultsOnly, Category = Curve)
		UCurveFloat* CurveFlick;



};
