s = "ннннфвалынфждываождн!!!!нннннн.нннннфваннннннннн"
curch = 0
m = 0
for i in range(len(s)):
    if s[i] == "н":
        curch += 1
    else: 
        m = max(m, curch)
        curch = 0
m = max(m, curch)
print(m)
s = s.replace("!", ".")
print(s)