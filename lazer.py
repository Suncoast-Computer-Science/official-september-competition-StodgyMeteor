players = int(input())
scores = []
realscores =  [ ]
for i in range(0, players):
 	scores.append(int(input()))
for i in range(0,players):
 	if i%2 ==0 :
		  realscores.append(scores[i] + scores[i+1])
realscores.sort()
