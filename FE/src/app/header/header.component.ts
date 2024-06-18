import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    console.log('on init');
  }

  loginButton(): void {
    this.apiService.getApi().subscribe(
      response => {
        console.log('API response:', response);
      },
      error => {
        console.error('API error:', error);
      }
    );
    console.log('Accesso 2');
  }

  registerButton(): void {
    console.log('Registrati button clicked');
  }
}
