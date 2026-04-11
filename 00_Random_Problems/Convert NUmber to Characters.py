def number_to_words(n):
    ones = ["", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"]
    teens = ["Ten","Eleven", "Twelve", "Thirteen", "Fourteen", "Fifeteen",
    "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
    tens = ["", "", "Twenty", "Thirty", 'Fourty','Fifety', 'Sixty', 'Seventy','Eighty', 'Ninety']
    
    if n == 0:
        return "Zore"
    def helper(num):
        if num == 0:
            return ""
        elif num < 10:
            return ones[num]
        elif num < 20:
            return teens[num-10]
        elif num < 100:
            return tens[num//10]+" "+helper(num%10)
        elif num < 1000:
            return ones[num // 100]+" Hundred "+helper(num%100)
        elif num < 10000:
            return tens[num//1000]+" Thousand "+helper(num%1000)
    return helper(n).strip()
    
print(number_to_words(9999))