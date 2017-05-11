run:
	python3 TitleManager.py

doc:
	pydoc3 TitleNode.py > TitleNode.txt
	pydoc3 TitleManager.py > TitleManager.txt

clean:
	find -name "*~" -type f -exec rm -vf '{}' \;
