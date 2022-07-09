import statistics


# グルコース定量法
class GlucoseQuantitative:
    def absorbance_average(self, x_1, x_2):
        absorbance_l = [x_1, x_2]
        x_average = statistics.mean(absorbance_l)
        return x_average


    # 血漿の平均吸光度-NC群の平均吸光度→NADPHのモル吸光係数
    def net_absorbance(self, x_average, y_average):
        net = x_average - y_average
        return net

    # A は吸光度、eはモル吸光係数、cは媒質のモル濃度:A=ecl
    def lambert_beer_mol(self, A: int, e: int, l: int):
        c = A / (e * l)
        return c

    # 1mMを_mg/dlに変換する。Mは対象物質の分子量
    @classmethod
    def mM_to_mgdl(self,M:int):
        mM = M / 1000
        mg = mM * 1000
        mgdl = mg / 10
        return mgdl
g = GlucoseQuantitative()

A_1 = float(input("Aの血漿の1つ目の吸光度を入力してください。"))
A_2 = float(input("Aの血漿の2つ目の吸光度を入力してください。"))
A_average = g.absorbance_average(A_1, A_2)
print(str(A_average)+"：一番目の吸光度")
A_NC_1 = float(input("AのNCの1つ目の吸光度を入力してください。"))
A_NC_2 = float(input("AのNCの2つ目の吸光度を入力してください。"))
A_NC_average = g.absorbance_average(A_NC_1, A_NC_2)
print(str(A_NC_average)+ ":Aの平均脱イオン水の吸光度")
A_net_absorbance = g.net_absorbance(A_average, A_NC_average)
print(str(A_net_absorbance)+":正味の吸光度")

B_1 = float(input("Bの血漿の1つ目の吸光度を入力してください。"))
B_2 = float(input("Bの血漿の2つ目の吸光度を入力してください。"))
B_average = g.absorbance_average(B_1, B_2)
print(str(B_average)+ "：Bの吸光度の平均値")
B_NC_1 = float(input("BのNCの1つ目の吸光度を入力してください。"))
B_NC_2 = float(input("BのNCの2つ目の吸光度を入力してください。"))
B_NC_average = g.absorbance_average(B_NC_1, B_NC_2)
print(str(B_NC_average)+ ":Bの脱イオン水の吸光度の平均値")
B_net_absorbance = g.net_absorbance(B_average, B_NC_average)
print(str(B_net_absorbance)+ ":Bの正味の吸光度")

C_1 = float(input("Cの血漿の1つ目の吸光度を入力してください。"))
C_2 = float(input("Cの血漿の2つ目の吸光度を入力してください。"))
C_average = g.absorbance_average(C_1, C_2)
print(str(C_average)+ ":Cの血漿の吸光度の平均")
C_NC_1 = float(input("CのNCの1つ目の吸光度を入力してください。"))
C_NC_2 = float(input("CのNCの2つ目の吸光度を入力してください。"))
C_NC_average = g.absorbance_average(C_NC_1, C_NC_2)
print(str(C_NC_average)+":Cの脱イオン水の平均値")
C_net_absorbance = g.net_absorbance(C_average, C_NC_average)
print(str(C_net_absorbance)+ "Cの正味の吸光度")
# 6.22×10＾｛‐3｝M＾｛‐1｝cm｛‐1｝＝6.22mM^{-1}
NADPH_mol_absorbance = 6.22

A_NADPH_concentration = g.lambert_beer_mol(A=A_net_absorbance, e=NADPH_mol_absorbance, l=1)
B_NADPH_concentration = g.lambert_beer_mol(A=B_net_absorbance, e=NADPH_mol_absorbance, l=1)
C_NADPH_concentration = g.lambert_beer_mol(A=C_net_absorbance, e=NADPH_mol_absorbance, l=1)
Diluted_A_glucose_concentration = A_NADPH_concentration # グルコース濃度の単位は、mM
Diluted_B_glucose_concentration = B_NADPH_concentration
Diluted_C_glucose_concentration = C_NADPH_concentration
print("NADPHの濃度：" + str(A_NADPH_concentration))
x = g.mM_to_mgdl(M=180)
# 希釈倍数
Dilution_multiple = int(input("希釈倍率を入力してください。"))
A_glucose_concentration_mM = Diluted_A_glucose_concentration * Dilution_multiple
B_glucose_concentration_mM = Diluted_B_glucose_concentration * Dilution_multiple
C_glucose_concentration_mM = Diluted_C_glucose_concentration * Dilution_multiple
l_mM = [A_glucose_concentration_mM, B_glucose_concentration_mM, C_glucose_concentration_mM]
A_glucose_concentration_dl = A_glucose_concentration_mM * x
B_glucose_concentration_dl = B_glucose_concentration_mM * x
C_glucose_concentration_dl = C_glucose_concentration_mM * x
l_dl = [A_glucose_concentration_dl, B_glucose_concentration_dl, C_glucose_concentration_dl]

# 平均値
mean = statistics.mean(l_mM)
# 標準偏差
std_deviation = statistics.pstdev(l_dl)

print(str(mean)+ "±" + str(std_deviation) + "(n=3)")





