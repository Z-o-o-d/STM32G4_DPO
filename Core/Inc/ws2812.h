/*
 * @Description: WS2812驱动头文件
 * @Author: Tomood
 * @Date: 2024-03-25 23:07:58
 * @LastEditTime: 2024-06-15 15:21:21
 * @FilePath: \ARGB-ligtcontroller\bsp\ws2812.h
 */
#ifndef __WS2812_H
#define __WS2812_H
#include "main.h"

/*灯参数宏*/
#define WS2812_NUM               10                            	     //WS2812串联个数
#define WS2812_DATA_LEN          24                           		 //WS2812数据长度(RGB888 = 24bit)
#define WS2812_BUF_SIZE          (WS2812_NUM + 1) * WS2812_DATA_LEN  //ws2812级联后需要的数组长度(需要增加复位码)

/*WS2812对应码元的定时器计数值 PWM周期：800 kHz*/
#define High_Code             90                        //1 码相对计数值
#define Low_Code              45                        //0 码相对计数值

/*生成PWM的定时器和通道定义*/
#define WS2812_TIM  htim8
#define WS2812_CHANNEL  TIM_CHANNEL_3

extern uint16_t WS2812_Buf[];
extern uint8_t WS2812_Brightness;



// 定义位域结构体来表示 RGB 颜色
typedef struct {
    uint32_t red : 8;
    uint32_t green : 8;
    uint32_t blue : 8;
} RGBColor;

//基础控制函数
void WS2812_Write_Data(uint32_t Color, uint8_t index);
void WS2812_Set_All(uint32_t Color);
void WS2812_Update(void);
void WS2812_Write_Colors(RGBColor *colors, uint8_t count);

#endif
