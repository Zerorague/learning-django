import smtplib


def enviarCorreo(subject, from_addr, to_addrs, msg):
    # conexion con servidor
    conexion = smtplib.SMTP(host="smtp.gmail.com", port=587)
    conexion.ehlo()

    # tls

    conexion.starttls()

    # iniciar sesion en servidor smptp

    conexion.login(user="julioasmb@gmail.com", password="egrgbixogbmkszgz")

    conexion.sendmail(
        from_addr=from_addr, to_addrs=to_addrs, msg=f"Subject:{subject}\n{msg}"
    )

    # desconectar servidor

    conexion.quit()
