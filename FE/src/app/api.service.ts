import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  private apiUrl = 'http://127.0.0.1:4200/api/v1';

  constructor(private httpClient: HttpClient) {}

  getApi(): Observable<any> {
    return this.httpClient.get<any>(`${this.apiUrl}/prova`);
  }
}
