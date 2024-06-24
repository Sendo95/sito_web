import { Component } from '@angular/core';
import { ModaleAccessoComponent } from '../modale-accesso/modale-accesso.component';
import { MatDialog, MatDialogRef } from '@angular/material/dialog';
import { trigger, state, style, animate, transition } from '@angular/animations';

@Component({
  selector: 'app-modale-registrazione',
  templateUrl: './modale-registrazione.component.html',
  styleUrl: './modale-registrazione.component.css',
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
export class ModaleRegistrazioneComponent {

  name = '';
  surname = '';
  email = '';
  password = '';

  constructor(public registerModal: MatDialogRef<ModaleRegistrazioneComponent>,
              private dialog: MatDialog) { }

  ngOnInit(): void {
  }

  login(): void {
    this.registerModal.close()
  }

  closeDialog(): void {
    this.registerModal.close()
  }

  onAccedi(){
    this.registerModal.close();

    // setta il tempo per aprire la modale
    setTimeout(() => {
      const dialogRef = this.dialog.open(ModaleAccessoComponent, {
        width: '400px',
        disableClose: false,
        autoFocus: false
      });

      dialogRef.afterClosed().subscribe(result => {
        console.log('Modale di accesso chiusa', result);
      });
    }, 300); // imposta il tempo
  }

  onRegistrati(){
    this.registerModal.close()
  }

}
