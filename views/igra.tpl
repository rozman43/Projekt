%import model
%rebase("base.tpl", title="Mat_Quiz")

  <h1>Mat-Quiz</h1>

  <blockquote>
    <b>{{igra.trenutno_vprasanje()}}</b>
  </blockquote>

  <table>
    <tr>
      <td>
        Število napak: <b>{{igra.st_napacni_odgovori()}}</b>
      </td>
    </tr>
    <tr>  
      <td>
        Število pravilnih odgovorov: <b>{{igra.st_pravilni_odgovori()}}</b>
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
