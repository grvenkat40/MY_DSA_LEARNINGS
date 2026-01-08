class Solution:
    def reformatDate(self, date: str) -> str:
        months = {"Jan":"01", "Feb":"02", "Mar":"03", "Apr":"04", "May":"05", "Jun":"06", "Jul":"07", "Aug":"08", "Sep":"09", "Oct":"10", "Nov":"11", "Dec":"12"}
        given = date.split(" ")
        
        date = "" 
        if len(given[0]) == 3:
            date = "0"+given[0][:1]
        else:
            date = int(given[0][:2])
        month = months[given[1]]
        year = given[-1]
        result = year + "-" + month +  "-" + str(date)
        return result

obj = Solution()
date = "6th Jun 1933"
print(obj.reformatDate(date))