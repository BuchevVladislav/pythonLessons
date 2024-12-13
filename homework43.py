s = "фжыдшялчжфоцущшляждлаофлоащшуаавфыафжяяяфшуаолаоядафаожфдллыяаождлдав"
for i in range(len(s)):
    if s[i] == "а":
        for j in range(i, len(s)):
            if s[j] != "я": print(s[j], end="")
            else: 
                 print("\n")
                 break