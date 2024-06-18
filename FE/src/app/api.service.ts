import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  private apiUrl = 'http://localhost:8000'

  constructor(private httpClient: HttpClient) { }

  getApi(): Observable<any> {
    return this.httpClient.get<any>(this.apiUrl + '/api/v1/prova')
  }
  
}
