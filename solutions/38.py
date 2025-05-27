class Solution:
    def RLE(self, string):
            
        res = ""
        char = string[0]
        count = 1
        i = 0
        
        while i < len(string) - 1:
 
            if (char == string[i + 1]):
                count += 1
            
            else:
                res += str(count) + char
                count = 1
                char = string[i + 1]
                
            i += 1
            
        res += str(count) + char
                
                
        return res
    
    
    
    def countAndSay(self, n: int) -> str:
        
        if n == 1:
            return "1"
        
        return self.RLE(self.countAndSay(n - 1))