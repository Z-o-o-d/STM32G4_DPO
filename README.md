<!--
 * @Author: Zeee jinze2021@dgut.edu.cn
 * @Date: 2025-03-05 19:21:48
 * @LastEditors: Zeee jinze2021@dgut.edu.cn
 * @LastEditTime: 2025-03-07 06:49:52
 * @FilePath: \DPO1\README.md
 * @Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
-->
### 待改善

整点元子的取模设置，这个st7789只能写16位

![alt text](image.png)

字宽16的倍数，在下面这里调整

···
group_size = 3  # 可根据需要设置分组大小，例如 2、3、4 等
···

目前只能单个字转换

![alt text](image-1.png)