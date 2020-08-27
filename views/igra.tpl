%import model
%rebase("base.tpl", title="Kviz")

  <h1>Kviz</h1>

  <blockquote>
    <b>{{igra.trenutno_vprasanje}}</b>
  </blockquote>

  <table>
    <tr>
      <td>
        Število napak: <b>{{igra.napake()}}</b>
      </td>
    </tr>
    <tr>  
      <td>
        Število pravilnih odgovorov: <b>{{igra.pravilni()}}</b>
      </td>
    </tr>
  </table>

%if poskus == model.ZMAGA:
  <h1>ZMAGA!</h1>

  <form action="/nova_igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

%elif poskus == model.PORAZ:
  <h1>IZGUBILI STE!</h1>

  <form action="/nova_igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

%end

<form action="/igra/" method="post">
    Odgovor: <input type="text" name="odgovor">
    <button type="submit">Pošlji odgovor</button>
</form>

%end
