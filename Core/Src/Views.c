#include "Views.h"


extern ADC_HandleTypeDef hadc2;
extern ADC_HandleTypeDef hadc3;
extern ADC_HandleTypeDef hadc5;
extern DMA_HandleTypeDef hdma_adc2;
extern DMA_HandleTypeDef hdma_adc3;
extern DMA_HandleTypeDef hdma_adc5;

extern COMP_HandleTypeDef hcomp2;
extern COMP_HandleTypeDef hcomp5;

extern DAC_HandleTypeDef hdac1;
extern DAC_HandleTypeDef hdac2;
extern DAC_HandleTypeDef hdac4;

extern HRTIM_HandleTypeDef hhrtim1;

extern I2C_HandleTypeDef hi2c3;

extern UART_HandleTypeDef hlpuart1;

extern OPAMP_HandleTypeDef hopamp1;
extern OPAMP_HandleTypeDef hopamp2;
extern OPAMP_HandleTypeDef hopamp3;
extern OPAMP_HandleTypeDef hopamp5;
extern OPAMP_HandleTypeDef hopamp6;

extern SPI_HandleTypeDef hspi3;
extern DMA_HandleTypeDef hdma_spi3_tx;

extern TIM_HandleTypeDef htim1;
extern TIM_HandleTypeDef htim3;
extern TIM_HandleTypeDef htim4;
extern TIM_HandleTypeDef htim6;
extern TIM_HandleTypeDef htim7;
extern TIM_HandleTypeDef htim8;
extern TIM_HandleTypeDef htim15;
extern TIM_HandleTypeDef htim20;
extern DMA_HandleTypeDef hdma_tim8_ch3;
extern DMA_HandleTypeDef hdma_tim15_ch1;


extern FEAnalogStates FEAnalog;


extern uint32_t BUFFER_SYS_ADC[5];


extern unsigned char BUFFER_Display;


void View_KingKong(void){
		ST7789_DrawTriangle(20, 210, 40, 200, 40, 220, WHITE);
		ST7789_DrawCircle(90, 210, 10, WHITE);
		ST7789_DrawRectangle(140, 200, 160, 220, WHITE);
	}


void View_DoubaoWelcome(void){
		ST7789_DrawImage(10, 10, 160, 160, (uint16_t *)doubao);
		ST7789_WriteString(0, 180, " !\"#$\%&\'\(\)", Han_Array32, WHITE, BLACK);
//		ST7789_WriteString(170, 180, "", Han_Array, WHITE, BLACK);
	}


void View_Sensor(void){
	sprintf(&BUFFER_Display,"ENC1:%5d",htim4.Instance->CNT);
	ST7789_WriteString(200, 30, &BUFFER_Display, Font_11x18, WHITE, BLACK);
	sprintf(&BUFFER_Display,"ENC2:%5d",htim3.Instance->CNT);
	ST7789_WriteString(200, 50, &BUFFER_Display, Font_11x18, WHITE, BLACK);
	sprintf(&BUFFER_Display,"ENC3:%5d",htim20.Instance->CNT);
	ST7789_WriteString(200, 70, &BUFFER_Display, Font_11x18, WHITE, BLACK);
	sprintf(&BUFFER_Display,"ENC4:%5d",htim1.Instance->CNT);
	ST7789_WriteString(200, 100, &BUFFER_Display, Font_11x18, WHITE, BLACK);

	sprintf(&BUFFER_Display,"KEYs:%5d",BUFFER_SYS_ADC[0]);
	ST7789_WriteString(200, 130, &BUFFER_Display, Font_11x18, WHITE, BLACK);

	float temperate=(((float)BUFFER_SYS_ADC[1]*(3.3/4096)-0.76)/0.0025 + 30); //转换为温度值;
	sprintf(&BUFFER_Display,"TEMP:%4.1f",temperate);
	ST7789_WriteString(200, 160, &BUFFER_Display, Font_11x18, WHITE, BLACK);

	sprintf(&BUFFER_Display,"Vbat:%5d",BUFFER_SYS_ADC[2]);
	ST7789_WriteString(200, 190, &BUFFER_Display, Font_11x18, WHITE, BLACK);

	sprintf(&BUFFER_Display,"Vref:%5d",BUFFER_SYS_ADC[3]);
	ST7789_WriteString(200, 220, &BUFFER_Display, Font_11x18, WHITE, BLACK);

	}


void View_Config(void){

//	ST7789_Fill_Color(WHITE);
	sprintf(&BUFFER_Display,"ENC1:%5d",htim4.Instance->CNT);
	ST7789_WriteString(10, 10, "CONFIG", Font_16x26, WHITE, BLACK);
	sprintf(&BUFFER_Display,"ARGB:%5d",WS2812_Brightness);
	ST7789_WriteString(10, 40, &BUFFER_Display, Font_11x18, WHITE, BLACK);
	sprintf(&BUFFER_Display,"LCD :%5d",htim8.Instance->CCR1);
	ST7789_WriteString(10, 60, &BUFFER_Display, Font_11x18, WHITE, BLACK);

	sprintf(&BUFFER_Display,"AMP1:%5d",FEAnalog.CD_CH1);
	ST7789_WriteString(10, 80, &BUFFER_Display, Font_11x18, WHITE, BLACK);
	sprintf(&BUFFER_Display,"OFS1:%5d",FEAnalog.OFFSET1);
	ST7789_WriteString(10, 100, &BUFFER_Display, Font_11x18, WHITE, BLACK);
	sprintf(&BUFFER_Display,"AMP2:%5d",FEAnalog.CD_CH2);
	ST7789_WriteString(10, 120, &BUFFER_Display, Font_11x18, WHITE, BLACK);
	sprintf(&BUFFER_Display,"OFS2:%5d",FEAnalog.OFFSET2);
	ST7789_WriteString(10, 140, &BUFFER_Display, Font_11x18, WHITE, BLACK);
	sprintf(&BUFFER_Display,"CH  :%5d",CH_selected);
	ST7789_WriteString(10, 160, &BUFFER_Display, Font_11x18, WHITE, BLACK);
	sprintf(&BUFFER_Display,"DBG:%10d",DEBUG_TICK_COUNT);
	ST7789_WriteString(10, 180, &BUFFER_Display, Font_11x18, WHITE, BLACK);



	sprintf(&BUFFER_Display,"ENC1:%5d",htim4.Instance->CNT);
	ST7789_WriteString(170, 0, &BUFFER_Display, Font_11x18, WHITE, BLACK);
	sprintf(&BUFFER_Display,"ENC2:%5d",htim3.Instance->CNT);
	ST7789_WriteString(170, 20, &BUFFER_Display, Font_11x18, WHITE, BLACK);
	sprintf(&BUFFER_Display,"ENC3:%5d",htim20.Instance->CNT);
	ST7789_WriteString(170, 40, &BUFFER_Display, Font_11x18, WHITE, BLACK);
	sprintf(&BUFFER_Display,"ENC4:%5d",htim1.Instance->CNT);
	ST7789_WriteString(170, 60, &BUFFER_Display, Font_11x18, WHITE, BLACK);

	sprintf(&BUFFER_Display,"KEYs:%5d",BUFFER_SYS_ADC[0]);
	ST7789_WriteString(170, 100, &BUFFER_Display, Font_11x18, WHITE, BLACK);

	float temperate=(((float)BUFFER_SYS_ADC[1]*(3.3/4096)-0.76)/0.0025 + 30); //转换为温度值;
	sprintf(&BUFFER_Display,"TEMP:%4.1f",temperate);
	ST7789_WriteString(170, 120, &BUFFER_Display, Font_11x18, WHITE, BLACK);

	sprintf(&BUFFER_Display,"Vbat:%5d",BUFFER_SYS_ADC[2]);
	ST7789_WriteString(170, 140, &BUFFER_Display, Font_11x18, WHITE, BLACK);

	sprintf(&BUFFER_Display,"Vref:%5d",BUFFER_SYS_ADC[3]);
	ST7789_WriteString(170, 160, &BUFFER_Display, Font_11x18, WHITE, BLACK);

	}




void View_DPO(void){

//	ST7789_Fill_Color(WHITE);

	sprintf(&BUFFER_Display,"ARGB:%5d",WS2812_Brightness);
	ST7789_WriteString(10, 40, &BUFFER_Display, Font_11x18, WHITE, BLACK);


	}
