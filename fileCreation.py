filenames = ['doc.txt', 'report.txt', 'presentation.txt']
text = "Hello"
for filename in filenames:
    with open(filename,'w') as file:
        file.write(text)
