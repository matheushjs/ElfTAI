run:
	python3 TitleManager.py

doc:
	pydoc3 TitleNode > TitleNode.txt
	pydoc3 TitleManager > TitleManager.txt

clean:
	find -name "*~" -type f -exec rm -vf '{}' \;
