echo "Automated 303 Script to scrape for new links"

while true;
do
	# get HTML output of the repo
	wget https://github.com/jin-guo/COMP303_Winter2019 -O get1.txt ;

	# cuts the wget file to reduce runtime (only scan section that matters)
	cat get1.txt | grep '<a class="commit-tease-sha" href="/jin-guo/COMP303_Winter2019/' > update.txt ;

	# reduce space complexity
	rm get1.txt ;

	# trigger python script to send text if needed
	python3 303script.py ;

	# reduce space complexity
	rm update.txt ;

	# sleep cycle to ensure wget request does not get blocked // allows user to notice text
	sleep 60 ;
done

