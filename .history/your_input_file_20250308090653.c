typedef struct {
  // 使用位域来表示18个按键，每个按键占1位
  unsigned int KEY0 : 1;
  unsigned int KEY1 : 1;
  unsigned int KEY2 : 1;
  unsigned int KEY3 : 1;
  unsigned int KEY4 : 1;
  unsigned int KEY5 : 1;
  unsigned int ENC1_UP : 1;
  unsigned int ENC1_DOWN : 1;
  unsigned int ENC1_KEY : 1;
  unsigned int ENC2_UP : 1;
  unsigned int ENC2_DOWN : 1;
  unsigned int ENC2_KEY : 1;
  unsigned int ENC3_UP : 1;
  unsigned int ENC3_DOWN : 1;
  unsigned int ENC3_KEY : 1;
  unsigned int ENC4_UP : 1;
  unsigned int ENC4_DOWN : 1;
  unsigned int ENC4_KEY : 1;
  // xy坐标，假设使用足够表示相应范围的整数类型
  uint16_t touch_x;
  uint16_t touch_y;
} InputStruct;
