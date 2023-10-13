text = "I am honored to be with you today at your commencement from one of the finest universities in the world. I never graduated from college. Truth be told, this is the closest I’ve ever gotten to a college graduation. Today I want to tell you three stories from my life. That’s it. No big deal. Just three stories. The first story is about connecting the dots. I dropped out of Reed College after the first 6 months, but then stayed around as a drop-in for another 18 months or so before I really quit. So why did I drop out? It started before I was born. My biological mother was a young, unwed college graduate student, and she decided to put me up for adoption. She felt very strongly that I should be adopted by college graduates, so everything was all set for me to be adopted at birth by a lawyer and his wife. Except that when I popped out they decided at the last minute that they really wanted a girl. So my parents, who were on a waiting list, got a call in the middle of the night asking: “We have an unexpected baby boy; do you want him?” They said: “Of course.” My biological mother later found out that my mother had never graduated from college and that my father had never graduated from high school. She refused to sign the final adoption papers. She only relented a few months later when my parents promised that I would someday go to college. And 17 years later I did go to college. But I naively chose a college that was almost as expensive as Stanford, and all of my working-class parents’ savings were being spent on my college tuition. After six months, I couldn’t see the value in it. I had no idea what I wanted to do with my life and no idea how college was going to help me figure it out. And here I was spending all of the money my parents had saved their entire life. So I decided to drop out and trust that it would all work out OK. It was pretty scary at the time, but looking back it was one of the best decisions I ever made. The minute I dropped out I could stop taking the required classes that didn’t interest me, and begin dropping in on the ones that looked interesting."

alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

text = text.lower() #text내에 알파벳을 모두 소문자로 만들어줌

a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z = 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0 #알파벳에 숫자를 더할 것임으로 0으로 초기값 설정

#텍스트 내에 알파벳 매치하는 것 개수 확인 - for문을 활용
for jj in text:
    if "a" == jj:
        a += 1
    if "b" == jj:
        b += 1
    if "c" == jj:
        c += 1
    if "d" == jj:
        d += 1
    if "e" == jj:
        e += 1
    if "f" == jj:
        f += 1
    if "g" == jj:
        g += 1
    if "h" == jj:
        h += 1
    if "i" == jj:
        i += 1
    if "j" == jj:
        j += 1
    if "k" == jj:
        k += 1
    if "l" == jj:
        l += 1
    if "m" == jj:
        m += 1
    if "n" == jj:
        n += 1
    if "o" == jj:
        o += 1
    if "p" == jj:
        p += 1
    if "q" == jj:
        q += 1
    if "r" == jj:
        r += 1
    if "s" == jj:
        s += 1
    if "t" == jj:
        t += 1
    if "u" == jj:
        u += 1
    if "v" == jj:
        v += 1
    if "w" == jj:
        w += 1
    if "x" == jj:
        x += 1
    if "y" == jj:
        y += 1
    if "z" == jj:
        z += 1

#max를 활용하여 가장 많이 쓰인 알파벳과 쓰인 횟수 파악
bigalp = max(alphabet)
bignum = max(a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y,z)

print(f"가장 많이 사용된 알파벳은 {bigalp}이며 모두 {bignum}번 사용되었습니다.")