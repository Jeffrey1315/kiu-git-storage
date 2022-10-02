def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    temp1 = 273.15 + temp
    result = (given_mass1/molar_mass1 + given_mass2/molar_mass2) * temp1 * 0.082
    return (result/volume)
