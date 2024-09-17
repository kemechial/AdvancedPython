friends={"Jack","Bob","Allen"}

abroad={"Jeremy","Jack"}

local_firends=friends.difference(abroad)

print(local_firends)

all_friends=local_firends.union(abroad)

print(all_friends)

both=friends.intersection(abroad)

print(both)