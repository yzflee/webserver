import pstats
import pprint

# strip_dirs(): ȥ���޹ص�·����Ϣ
# sort_stats(): ����֧�ֵķ�ʽ��������һ��
# print_stats(): ��ӡ�������������ָ����ӡǰ����

# ��ֱ������cProfile.run("test()")�Ľ����һ����
#p.strip_dirs().sort_stats(-1).print_stats()

# ���պ���������ֻ��ӡǰ3�к�������Ϣ, ��������ΪС��,��ʾǰ�ٷ�֮���ĺ�����Ϣ
#p.strip_dirs().sort_stats("tottime").print_stats(3)

# ��������ʱ���������
#p.strip_dirs().sort_stats("cumulative").print_stats(1)

# �����֪������Щ����������sum_num
#p.print_callers(0.5, "sum_num")

# �鿴test()�����е�������Щ����
#p.print_callees("test")

p=pstats.Stats("profile\TriFusion_1847ae4755_0.prof")

p.strip_dirs().print_callers()  # ������ʾ��������Щ��������
p.strip_dirs().print_callees()  # ������ʾ�ĸ�������������Щ����