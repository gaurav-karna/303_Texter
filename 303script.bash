echo "Automated 303 Script to scrape for new links"

while true;
do
	wget https://github.com/jin-guo/COMP303_Winter2019 -O get1.txt ;

	cat get1.txt | grep '<a class="commit-tease-sha" href="/jin-guo/COMP303_Winter2019/' > update.txt ;

	rm get1.txt ;

	python3 303script.py ;

	rm update.txt ;

	sleep 60 ;
done

