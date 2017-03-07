import { Injectable } from '@angular/core';
import { Http, URLSearchParams } from '@angular/http';
import { environment } from '../environments/environment';
import 'rxjs/add/operator/map';

@Injectable()
export class ESDataService {

  constructor(private http: Http) { }

  apiUrl = `http://${environment.host}:5000/exam/api/v1.0`;

  getData() {
    let params: URLSearchParams = new URLSearchParams();

    params.set('openPorts', '151,443,80')
    return this.http.get(`${this.apiUrl}/data`, {
      search: params
    })
      .map(res => res.json());
  }

  getPorts() {
    let params: URLSearchParams = new URLSearchParams();
    return this.http.get(`${this.apiUrl}/port`)
      .map(res => res.json())
      .map(res => res.data);
  }
}
