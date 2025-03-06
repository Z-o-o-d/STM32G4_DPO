/*
 * @Description: WS2812驱动函数库
 * @Author: Tomood
 * @Date: 2024-06-15 15:06:48
 * @LastEditors: Tomood
 * @LastEditTime: 2024-06-17 23:25:58
 * @FilePath: \undefinede:\STM32project\ARGB-ligtcontroller\bsp\ws2812.c
 * Copyright (c) 2024 by Tomood, All Rights Reserved.
 */
#include "ws2812.h"
#include "main.h"
#include "stm32g4xx_hal_tim.h"
#include "stdio.h"
#include <math.h>

//WS2812 DMA缓存数组
uint16_t WS2812_Buf[WS2812_BUF_SIZE] = { 0 };
extern TIM_HandleTypeDef WS2812_TIM;



/**
 * @brief  单个灯数据更新
 * @param  Color:颜色24bit of RGB888
 * @param  index:灯的标号
 * @return None
 */
void WS2812_Write_Data(uint32_t Color, uint8_t index)
{
    for (uint8_t i = 0; i < 24; i++)
		WS2812_Buf[24 * index + i] = (((Color << i) & 0X800000) ? High_Code : Low_Code);
}

/**
 * @brief  所有灯数据更新
 * @param  Color:颜色24bit of RGB888
 * @return None
 */
void WS2812_Set_All(uint32_t Color)
{
	/*循环写入所有灯珠数组*/
	for(uint8_t index = 0; index < WS2812_NUM; index++)
		WS2812_Write_Data(Color,index);
}

/**
 * @brief  WS2812更新指令
 * @param  None
 * @return None
 */
void WS2812_Update(void)
{
	HAL_TIM_PWM_Start_DMA(&WS2812_TIM,WS2812_CHANNEL,(uint32_t *)WS2812_Buf,WS2812_BUF_SIZE);
}


//DMA传输完成中断Callback
//void HAL_TIM_PWM_PulseFinishedCallback(TIM_HandleTypeDef *htim)
//{
//	HAL_TIM_PWM_Stop_DMA(&WS2812_TIM,WS2812_CHANNEL);
//}
