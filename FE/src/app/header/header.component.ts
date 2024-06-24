import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { MatDialog } from '@angular/material/dialog';
import { ModaleAccessoComponent } from '../modale-accesso/modale-accesso.component';
import { ModaleRegistrazioneComponent } from '../modale-registrazione/modale-registrazione.component';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {

  constructor(private apiService: ApiService,
              public dialog: MatDialog) {}

  ngOnInit(): void {
    
  }

  loginButton() {
    /*this.apiService.getApi().subscribe(
      response => {
        console.log('API response:', response);
      },
      error => {
        console.error('API error:', error);
      }
    );*/
    
    //al click mi apre la modale
    const loginModal = this.dialog.open(ModaleAccessoComponent, {
      width: '400px'
    });

    loginModal.afterClosed().subscribe(result => {
      console.log('Modal chiuso');
    });
    
  }

  registerButton() {
    //al click mi apre la modale
    const registerModal = this.dialog.open(ModaleRegistrazioneComponent, {
      width: '400px'
    });

    registerModal.afterClosed().subscribe(result => {
      console.log('Modal chiuso');
    });
  }
}
