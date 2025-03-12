/* USER CODE BEGIN Header */
/**
  ******************************************************************************
  * @file           : main.h
  * @brief          : Header for main.c file.
  *                   This file contains the common defines of the application.
  ******************************************************************************
  * @attention
  *
  * Copyright (c) 2025 STMicroelectronics.
  * All rights reserved.
  *
  * This software is licensed under terms that can be found in the LICENSE file
  * in the root directory of this software component.
  * If no LICENSE file comes with this software, it is provided AS-IS.
  *
  ******************************************************************************
  */
/* USER CODE END Header */

/* Define to prevent recursive inclusion -------------------------------------*/
#ifndef __MAIN_H
#define __MAIN_H

#ifdef __cplusplus
extern "C" {
#endif

/* Includes ------------------------------------------------------------------*/
#include "stm32g4xx_hal.h"

/* Private includes ----------------------------------------------------------*/
/* USER CODE BEGIN Includes */
#include "MyLib.h"
/* USER CODE END Includes */

/* Exported types ------------------------------------------------------------*/
/* USER CODE BEGIN ET */

/* USER CODE END ET */

/* Exported constants --------------------------------------------------------*/
/* USER CODE BEGIN EC */

/* USER CODE END EC */

/* Exported macro ------------------------------------------------------------*/
/* USER CODE BEGIN EM */

/* USER CODE END EM */

void HAL_HRTIM_MspPostInit(HRTIM_HandleTypeDef *hhrtim);

void HAL_TIM_MspPostInit(TIM_HandleTypeDef *htim);

/* Exported functions prototypes ---------------------------------------------*/
void Error_Handler(void);

/* USER CODE BEGIN EFP */

/* USER CODE END EFP */

/* Private defines -----------------------------------------------------------*/
#define AC_DC_CH2_Pin GPIO_PIN_13
#define AC_DC_CH2_GPIO_Port GPIOC
#define CD_CH2_A_Pin GPIO_PIN_14
#define CD_CH2_A_GPIO_Port GPIOC
#define CD_CH2_B_Pin GPIO_PIN_15
#define CD_CH2_B_GPIO_Port GPIOC
#define CD_CH2_C_Pin GPIO_PIN_1
#define CD_CH2_C_GPIO_Port GPIOA
#define AC_DC_CH1_Pin GPIO_PIN_5
#define AC_DC_CH1_GPIO_Port GPIOA
#define CD_CH1_A_Pin GPIO_PIN_5
#define CD_CH1_A_GPIO_Port GPIOC
#define CD_CH1_B_Pin GPIO_PIN_15
#define CD_CH1_B_GPIO_Port GPIOB
#define CD_CH1_C_Pin GPIO_PIN_8
#define CD_CH1_C_GPIO_Port GPIOA
#define ADC_KEY_Pin GPIO_PIN_9
#define ADC_KEY_GPIO_Port GPIOA
#define ST7789_DC_Pin GPIO_PIN_11
#define ST7789_DC_GPIO_Port GPIOC
#define FT6336_RST_Pin GPIO_PIN_2
#define FT6336_RST_GPIO_Port GPIOD
#define TLC5952_SCLK_Pin GPIO_PIN_3
#define TLC5952_SCLK_GPIO_Port GPIOB
#define TLC5952_LAT_Pin GPIO_PIN_4
#define TLC5952_LAT_GPIO_Port GPIOB
#define TLC5952_SIN_Pin GPIO_PIN_5
#define TLC5952_SIN_GPIO_Port GPIOB

/* USER CODE BEGIN Private defines */


#define DDS_Onboard_TIM_HandleTypeDef HRTIM_TIMERINDEX_TIMER_C
#define DDS_Onboard_TIM_CH HRTIM_COMPAREUNIT_1

#define LCD_BRIGHTNESS TIM8

typedef struct {
  uint8_t KEY0      ;
  uint8_t KEY1      ;
  uint8_t KEY2      ;
  uint8_t KEY3      ;
  uint8_t KEY4      ;
  uint8_t KEY5      ;
  uint8_t KEY_ENC0  ;
  uint8_t KEY_ENC1  ;
  uint8_t KEY_ENC2  ;
  uint8_t KEY_ENC3  ;

  uint8_t Touched  ;

  uint16_t touch_x;
  uint16_t touch_y;
} Input_HandleTypeDef;


typedef struct {
	uint8_t AC_DC_CH1 ;
	uint8_t AC_DC_CH2 ;
	uint32_t CD_CH1 ;
	uint32_t CD_CH2 ;
	uint32_t OFFSET1 ;
	uint32_t OFFSET2 ;
} FEAnalogStates;


extern uint8_t CH_selected;
/* USER CODE END Private defines */

#ifdef __cplusplus
}
#endif

#endif /* __MAIN_H */
