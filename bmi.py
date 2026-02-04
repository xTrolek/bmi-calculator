import time
masa = int(input("podaj swoją mase w kg"))
wzrost = int(input("podaj swój wzrost w cm")) 
wzrost_1 = wzrost/100
wzrost_2 = wzrost_1 * wzrost_1
bmi = masa/wzrost_2
print("twoje bmi wynosi:",bmi)
print("\n")
time.sleep(1)
print("w zaokrągleniu wynosi:",round(bmi,1))
