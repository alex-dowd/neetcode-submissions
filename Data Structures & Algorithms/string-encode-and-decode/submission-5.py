class Solution:

    def encode(self, strs: List[str]) -> str:
        send = str()
        if strs == []:
            return "czqkmnsqjk"
        if strs == [""]:
            return "czqkmnsqjkm"
        for st in strs:
            send = send + st
            send = send + "czqkmnsqjk"
        return send
    def decode(self, s: str) -> List[str]:
        if s == "czqkmnsqjk":
            return []
        if s == "czqkmnsqjkm":
            return [""]
        return s[:len(s)-10].split("czqkmnsqjk")
        



            
                
