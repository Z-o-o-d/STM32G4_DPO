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
uint8_t WS2812_Brightness = 10;




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

// 将位域结构体转换为 uint32_t 类型
uint32_t RGBColorToUint32(RGBColor color) {
    return (color.red << 16) | (color.green << 8) | color.blue;
}


/**
 * @brief Write a series of RGB colors to WS2812 with brightness adjustment.
 * @param colors Pointer to the original RGBColor array.
 * @param count Number of elements in the array.
 * @return None
 */
void WS2812_Write_Colors(RGBColor *colors, uint8_t count) {
    for (uint8_t i = 0; i < count; i++) {
        uint32_t color_value = RGBColorToUint32(colors[i]);
        // 分离出 RGB 各通道
        uint8_t red = (color_value >> 16) & 0xFF;
        uint8_t green = (color_value >> 8) & 0xFF;
        uint8_t blue = color_value & 0xFF;

        // 调整各通道亮度
        red = (uint16_t)red * WS2812_Brightness / 255;
        green = (uint16_t)green * WS2812_Brightness / 255;
        blue = (uint16_t)blue * WS2812_Brightness / 255;

        // 重新组合成 uint32_t 类型
        color_value = ((uint32_t)red << 16) | ((uint32_t)green << 8) | blue;

        WS2812_Write_Data(color_value, i);
    }
    WS2812_Update();
}

