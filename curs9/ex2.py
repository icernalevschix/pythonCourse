import io

f = io.StringIO('My initial data')
print(f.getvalue())

f = io.BytesIO()
f.write(b'My Binary data')
print(f.getvalue())

f = io.StringIO('My initial data')
f.write('New Data')
print(f.getvalue())

f = io.StringIO('My initial data')
f.seek(0, io.SEEK_END)
f.write('New line 1')
f.write('New line 2')
print(f.getvalue())

f = io.StringIO('My initial data')
print(f.getvalue())
f.truncate(0)
print(f.getvalue())