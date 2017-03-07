import { Injectable } from '@angular/core';
import { Http, URLSearchParams } from '@angular/http';
import 'rxjs/add/operator/map';

@Injectable()
export class ESDataService {

  constructor(private http: Http) { }

  getData() {
    let params: URLSearchParams = new URLSearchParams();

    params.set('openPorts', '151,443,80')
    return this.http.get('http://localhost:5000/exam/api/v1.0/data', {
      search: params
    })
      .map(res => res.json());
  }

  getPorts() {
    let params: URLSearchParams = new URLSearchParams();
    return this.http.get('http://localhost:5000/exam/api/v1.0/port')
      .map(res => res.json())
      .map(res => res.data);
  }
}
