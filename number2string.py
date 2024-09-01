class NumbertoWord:
    def __init__(self):
        # Se definen las unidades
        self.units = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine']
        self.ten = ['Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']
        self.tens = ['', '', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        self.other = ['Hundred']


    def number2string(self, data: int) -> str:
        #turn variable in str to check if it's a negative numbre
        minus=str(data)
        
        #handle error out of range number
        if data >=10**33:
            raise NumberOutOfRangeException('Number out of range')
        
        #checks if it's a negative number
        if minus[0] =='-':
            newData = minus[1:]
            return ' '.join(['Minus',self.number2string(int(newData))])
        
        if data <10:
            return self.units[data]
        
        if 9 <data <20:
            return self.ten[data-10]
        
        if 19<data<100:
            dec = data//10
            unit = data % 10
            if unit == 0:
                return self.tens[dec]
            return ' '.join([self.tens[dec], self.units[unit]]).strip()
        if 99< data< 1000:
            dec = data//100
            un = data % 100
            if un == 0:
                return ' '.join([self.units[dec], self.other[0]]).strip()
            return ' '.join([self.units[dec], self.other[0], self.number2string(un)]).strip()
        
        #when are values greater than One Thousand
        # makes the exact divition of the data parameter and one of the variables below
        trillion = data//1000000000000
        billion = (data - trillion * 1000000000000) // 1000000000
        million = (data - trillion * 1000000000000 - billion * 1000000000 )//1000000
        thousand = (data - trillion * 1000000000000 - billion * 1000000000 - million * 1000000 )//1000
        #in case data parameter is less than any of the variables above
        remainder = data - trillion * 1000000000000 - billion * 1000000000 - million * 1000000 - thousand * 1000 
        
        result = []
        
        #check if is true (variable != 0) in any of the cases

        # it have to be in this order greater to less beacuse 
        # when the case it's true, the program append to the variable result
        # and pass to the next case 
        if trillion:
            result.append(self.number2string(trillion) + ' Trillion')
        if billion:
            result.append(self.number2string(billion) + ' Billion')
        if million:
            result.append(self.number2string(million) + ' Million')
        if thousand:
            result.append(self.number2string(thousand) + ' Thousand')
        if remainder:
            result.append(self.number2string(remainder))
        #at the end it join the data of the result array and separate each one
        # with a space
        return ' '.join(result).strip()

# Exception out of range class that heredate Exception class 
class NumberOutOfRangeException(Exception):
    pass

