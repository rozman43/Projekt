%import model
%rebase("base.tpl", title="Mat_Quiz")

<h1>Mat-Quiz</h1>

%if poskus == model.ZMAGA:
  <h1>Bravo! Zmagali ste.</h1> 
  <h3>Dobite 3 dodatne točke.</h3>
  <b>Za začetek nove igre kliknite na gumb Nova igra.</b>
  <h3> </h3>

  <form action="/nova_igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>

%elif poskus == model.PORAZ:
  <h1>Žal ste izgubili.</h1>
  <h3> Odšteli vam bomo 2 odstotni točki</h3>
  <b>Za začetek nove igre kliknite na gumb Nova igra.</b>
  <h3> </h3>

  <form action="/nova_igra/" method="post">
    <button type="submit">Nova igra</button>
  </form>
 
%else:
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

<form action="/igra/" method="post">
    Odgovor: <input type="text" name="odgovor">
    <button type="submit">Pošlji odgovor</button>
</form>

%end
