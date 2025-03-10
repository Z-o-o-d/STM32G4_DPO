/*
 * @Author: Zeee jinze2021@dgut.edu.cn
 * @Date: 2025-03-07 06:02:59
 * @LastEditors: Zeee jinze2021@dgut.edu.cn
 * @LastEditTime: 2025-03-10 21:34:48
 * @FilePath: \DPO1\your_output_file.c
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置
 * 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
 */
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