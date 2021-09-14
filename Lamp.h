// Fill out your copyright notice in the Description page of Project Settings.

#pragma once

#include "CoreMinimal.h"
#include "GameFramework/Actor.h"
#include "Containers/Array.h"
#include "Components/LightComponent.h"
#include "Components\TimelineComponent.h"
#include "Lamp.generated.h"

UENUM(BlueprintType)
enum class LumensType : uint8 {
	NoLumen UMETA(DisplayName = "NoLumen"),
	Bulb450 UMETA(DisplayName = "Bulb450"),
	Bulb800 UMETA(DisplayName = "Bulb800"),
	Bulb1100 UMETA(DisplayName = "Bulb1100"),
	Bulb1600 UMETA(DisplayName = "Bulb1600"),
	Bulb2600 UMETA(DisplayName = "Bulb2600"),
	Bulb5800 UMETA(DisplayName = "Bulb5800")
};


UCLASS(Blueprintable)
class UE5_INICIAL_API ALamp : public AActor
{
	GENERATED_BODY()
	
public:	
	// Sets default values for this actor's properties
	ALamp();
	UFUNCTION(BlueprintCallable, Category = "Control Lamp")
	void LightOn();
	UFUNCTION(BlueprintCallable, Category = "Control Lamp")
	void LightOff();
	UFUNCTION(BlueprintCallable, Category = "Control Lamp")
	void Flirck();
	UFUNCTION(BlueprintCallable, Category = "Control Lamp")
		float GetLumenByType();
	UFUNCTION(BlueprintCallable, Category = "Control Lamp")
		void ConfigurationLamp(float Emission,float Opacity);
	UPROPERTY(EditAnywhere)
		UCurveFloat* OnCurve;
	UTimelineComponent* MyTimeline;
	UFUNCTION()
		void ExecuteTimeline();
	UFUNCTION()
		void OnFinishTimline();
	float TimelineValue;
	float CurveValue;

protected:
	// Called when the game starts or when spawned
	virtual void BeginPlay() override;

public:	
	// Called every frame
	virtual void Tick(float DeltaTime) override;

	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Control Lamp")
		UStaticMeshComponent* LampMesh;
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Control Lamp")
		TArray<ULightComponent*> LightsLamp;
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Control Lamp")
		float IntensityOn;
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Control Lamp")
		float EmissionIntesity;
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Control Lamp")
		float OpacityIntesity;
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Control Lamp")
	 FName ParamEmissionName = FName(TEXT("EmissionIntesity"));
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Control Lamp")
		FName ParamOpacity = FName(TEXT("ParamOpacity"));
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Control Lamp")
		int32 indexOfMaterial = 0;
	UPROPERTY(EditAnywhere, BlueprintReadWrite, Category = "Control Lamp")
		LumensType lumensLamp;
	UMaterialInstanceDynamic* DynMaterial;

};
