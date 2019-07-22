from escpos.printer import Usb
p = Usb(0x0483, 0x5743, 0)
p.text("Hello World\n")
p.text("Lorem ipsum "*100)
p.qr("http://www.google.it",size=10)
p.barcode('1324354657687', 'EAN13', 64, 2, '', '')
p.text('\n'*2)
p.cut()
