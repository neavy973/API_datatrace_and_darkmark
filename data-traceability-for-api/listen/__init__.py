from listen.bf_function import my_audit_full, my_audit_distinct, original_distinct, original_full, for_full, \
    for_distinct
from listen.sniff_function import my_listen_distinct, my_listen_full
import time
if __name__ == '__main__':
    # start_time=time.time()

    # 监听
    # my_listen_full()
    # my_listen_distinct()

    # 初始最快方法，小数据量友好，大数据内存无法负担
    # 1.92    85.60
    # 0.66    24.47
    for_full('../user_data/leak_data.txt', 7, ['email', '姓名', '性别','手机号','省或直辖市', '市', '区或县'])
    # for_distinct('../user_data/leak_data.txt', 7, ['email', '姓名', '性别','手机号','省或直辖市', '市', '区或县'])

    # 使用bf_set的情况下，按100条数据从数据库中取出，存入bf_set，大数据情况下适用良好，速度快
    # 3.75    68.28
    # 1.70    24.96
    # my_audit_full('../user_data/leak_data.txt', 7, ['email', '姓名', '性别','手机号','省或直辖市', '市', '区或县'])
    # my_audit_distinct('../user_data/leak_data.txt', 7, ['email', '姓名', '性别','手机号','省或直辖市', '市', '区或县'])

    # 大数据情况下如果无法将数据全部读出，则将比对交给mysql，速度大大减慢
    # 234.24
    # 93.01
    # original_full('../user_data/leak_data.txt', 7, ['email', '姓名', '性别','手机号','省或直辖市', '市', '区或县'])
    # original_distinct('../user_data/leak_data.txt', 7, ['email', '姓名', '性别','手机号','省或直辖市', '市', '区或县'])

    # for_full()

    # end_time=time.time()
    # print("运行时间：",end_time-start_time,"秒")