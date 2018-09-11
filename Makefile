data=./original-data/movielens.dataset
out=./output
python=./python

mkuser=$(python)/mkuser.py
mkitem=$(python)/mkitem.py
mkdata=$(python)/mkdata.py

rawuser=$(data)/u.user
rawitem=$(data)/u.item
rawdata=$(data)/u.data

userfeature=$(out)/user.feature
itemfeature=$(out)/item.feature
allfeature=$(out)/all.feature

userdata=$(out)/user.data
itemdata=$(out)/item.data
alldata=$(out)/all.data

user: $(userfeature) $(userdata)

item: $(itemfeature) $(itemdata)

all: $(allfeature) $(alldata)

$(userfeature) $(userdata): $(mkuser) $(rawuser)
	cat $(rawuser) | $(mkuser) $(userfeature) > $(userdata)

$(itemfeature) $(itemdata): $(mkitem) $(rawitem)
	cat $(rawitem) | $(mkitem) $(itemfeature) > $(itemdata)

$(allfeature) $(alldata): $(userfeature) $(userdata) $(itemfeature) $(itemdata)
	cat $(rawdata) | $(mkdata) $(userfeature) $(userdata) \
		$(itemfeature) $(itemdata) $(allfeature) > $(alldata)
