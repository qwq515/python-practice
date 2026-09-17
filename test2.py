grade = [23,30,40]

if grade:
         g_len = 0
         g_sum = 0
         g_max = grade[0]
         g_min = grade[0]
         g_ql = 0
         g_uql = 0
         
         for score in grade:
            if score >= 60:
                g_ql += 1
                
            else:
                 g_uql += 1
            if score > g_max:
                g_max = score
            if score < g_min:
                g_min = score
            g_len += 1
            g_sum += score

         g_avg = g_sum/g_len

         print(g_max,g_min)
         print(g_avg)
         print(g_ql,g_uql)
          

else:
    print("未输入成绩")

