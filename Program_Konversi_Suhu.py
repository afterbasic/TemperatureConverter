#konversi suhu python
print("//PROGRAM KONVERSI SUHU PYTHON");
SYSTEM_OPERATOR_DATA_INPUT_CELCIUS = float(input("-Masukan suhu dalam celcius: "));
print("Suhu yang anda masukan adalah: ", SYSTEM_OPERATOR_DATA_INPUT_CELCIUS,"°c");
Operator_Data_Reamur = (4*(1/5))*SYSTEM_OPERATOR_DATA_INPUT_CELCIUS;
print("=Suhu dalam reamur: ", Operator_Data_Reamur);
Operator_Data_Kelvin = SYSTEM_OPERATOR_DATA_INPUT_CELCIUS + 273.15;
print("=Suhu dalam kelvin: ", Operator_Data_Kelvin);
Operator_Data_Fahrenheit = ((9*(1/5))*SYSTEM_OPERATOR_DATA_INPUT_CELCIUS)+32;
print("=Suhu dalam fahrenheit : ", Operator_Data_Fahrenheit);

#Konversi reamur

SYSTEM_OPERATOR_DATA_INPUT_REAMUR = float(input("Masukan suhu dalam reamur: "));
print("Suhu yabg anda masukan adalah ", SYSTEM_OPERATOR_DATA_INPUT_REAMUR,"°R");
System_Reamur_TO_Celcius = (5*(1/4))*SYSTEM_OPERATOR_DATA_INPUT_REAMUR;
print("=Suhu dalam celcius: ", System_Reamur_TO_Celcius,"°C");
System_Reamur_TO_Kelvin = ((5*(1/4))*SYSTEM_OPERATOR_DATA_INPUT_REAMUR)+273;
print("=Suhu dalam kelvin: ", System_Reamur_TO_Kelvin,"°K");
System_Reamur_TO_Fahrenheit = ((9*(1/4))*SYSTEM_OPERATOR_DATA_INPUT_REAMUR)+32;
print("=Suhu dalam fahrenheit: ", System_Reamur_TO_Fahrenheit,"°F");

#fahrenheit

SYSTEM_OPERATOR_DATA_INPUT_FAHRENHEIT = float(input("Masukan suhu dalam fahrenheit: "));
print("Suhu yang anda masukan adalah: ", SYSTEM_OPERATOR_DATA_INPUT_FAHRENHEIT, "°F");
System_Fahrenheit_TO_Celcius = (5*(1/9))*(SYSTEM_OPERATOR_DATA_INPUT_FAHRENHEIT-32);
print("=Suhu dalam celcius: ", System_Fahrenheit_TO_Celcius,"°C");
System_Fahrenheit_TO_Reamur = (4*(1/9))*(SYSTEM_OPERATOR_DATA_INPUT_FAHRENHEIT-32);
print("=Suhu dalam reamur: ", System_Fahrenheit_TO_Reamur, "°R");

#kelvin

SYSTEM_OPERATOR_DATA_INPUT_KELVIN = float(input("Masukan suhu dalam kelvin: "));
print("Suhu yang anda masukan adalah: ", SYSTEM_OPERATOR_DATA_INPUT_KELVIN, "°K");
System_Kelvin_TO_Celcius = SYSTEM_OPERATOR_DATA_INPUT_KELVIN - 273;
print("=Suhu dalam celcius: ", System_Kelvin_TO_Celcius, '°C');
System_Kelvin_TO_Reamur = (4*(1/5))*(SYSTEM_OPERATOR_DATA_INPUT_KELVIN-273);
print("=Suhu dalam reamur: ", System_Kelvin_TO_Reamur, "°R");
System_Kelvin_TO_Fahrenheit = (4*(1/5))*(SYSTEM_OPERATOR_DATA_INPUT_KELVIN-273)+32;
print("=Suhu dalam fahrenheit: ", System_Kelvin_TO_Fahrenheit);
print("//Thanks for using our software. ©2021 AfterBasic, Inc.");