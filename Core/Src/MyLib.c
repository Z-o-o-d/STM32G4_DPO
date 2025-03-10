#include "mylib.h"


void handle_overflow(uint32_t *value, int32_t delta, uint32_t lower_limit, uint32_t upper_limit) {
    if (delta >= 0) {
        // 当 delta 为正数，做加法操作，需要检查是否会超过上限
        if (upper_limit - *value < (uint32_t)delta) {
            // 如果加上 delta 会超过上限，将 value 设置为上限
            *value = upper_limit;
        } else {
            // 否则正常加上 delta
            *value += (uint32_t)delta;
        }
    } else {
        // 当 delta 为负数，做减法操作，需要检查是否会低于下限
        uint32_t abs_delta = (uint32_t)(-delta);
        if (*value < lower_limit + abs_delta) {
            // 如果减去 delta 的绝对值会低于下限，将 value 设置为下限
            *value = lower_limit;
        } else {
            // 否则正常减去 delta 的绝对值
            *value -= abs_delta;
        }
    }
}
