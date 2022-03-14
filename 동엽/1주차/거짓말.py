N,M = map(int,input().split())

know = list(map(int,input().split()))[1:]
visit = [0]*N

for k in know:
    visit[k-1] = 1 #진실을 알면 1로
parties = []

for _ in range(M):
    guests = list(map(int,input().split()))[1:]
    parties.append(guests)

party_visit = [0] *M

while know:
    known_guest = know.pop()
    candidate = set()

    for party_idx in range(len(parties)):
        party = set(parties[party_idx]) #해당 파티에 참여자
        if known_guest in party:
            candidate = candidate.union(party)#진실 파티에 참여자
            party_visit[party_idx] = 1#진실 말해야하는 파티
    
    for guest in candidate:
        if not visit[guest-1]:
            know.append(guest)
            visit[guest-1] = 1

print(party_visit.count(0))
