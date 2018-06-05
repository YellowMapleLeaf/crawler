from xml.dom import minidom


doc = minidom.parse('xml_doc.xml')
root=doc.documentElement
books = root.getElementsByTagName('book')
# print(books[0].childNodes[0])
for book in books:
    title=book.getElementsByTagName('title')[0].childNodes[0].nodeValue.strip()
    price=book.getElementsByTagName('price')[0].childNodes[0].nodeValue.strip()
    print(title,price)
    print(book.getElementsByTagName('title')[0].childNodes[1].childNodes[0].nodeValue)







