import { Component, OnInit } from '@angular/core';
import { MatDialog, MatDialogRef } from '@angular/material/dialog';
import { ModaleRegistrazioneComponent } from '../modale-registrazione/modale-registrazione.component';
import { trigger, state, style, animate, transition } from '@angular/animations';

@Component({
  selector: 'app-modale-accesso',
  templateUrl: './modale-accesso.component.html',
  styleUrls: ['./modale-accesso.component.css'],
  //animazione tra un'apertura di una modale e l'altra
  animations: [
    trigger('fadeInOut', [
      transition(':enter', [
        style({ opacity: 0 }),
        animate('300ms ease-in', style({ opacity: 1 }))
      ]),
      transition(':leave', [
        style({ opacity: 1 }),
        animate('300ms ease-out', style({ opacity: 0 }))
      ])
    ])
  ]
})
export class ModaleAccessoComponent implements OnInit {
  email = '';
  password = '';

  constructor(public loginModal: MatDialogRef<ModaleAccessoComponent>,
              private dialog: MatDialog) { }

  ngOnInit(): void {
  }

  login(): void {
    this.loginModal.close()
  }

  closeDialog(): void {
    this.loginModal.close()
  }

  onAccedi(){
    this.loginModal.close()
  }
  passwordDimenticata(){
    console.log("Password dimenticata")
  }
  onRegistrati(){
    this.loginModal.close();

    // setta il tempo per aprire la modale
    setTimeout(() => {
      const dialogRef = this.dialog.open(ModaleRegistrazioneComponent, {
        width: '400px',
        disableClose: false,
        autoFocus: false
      });

      dialogRef.afterClosed().subscribe(result => {
        console.log('Modale di registrazione chiusa', result);
      });
    }, 300);// imposta il tempo
  }
}
