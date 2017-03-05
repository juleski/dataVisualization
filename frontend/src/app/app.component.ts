import { Component, OnInit } from '@angular/core';
import { ESDataService } from './esdata.service';
import { DatePipe } from '@angular/common';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {

  private portList = {};
  private storage = {};
  private dateList = [];

  // UI Vars
  public barChartLabels:string[];
    public barChartData:any[] = [
    {data: [0, 0]}
  ];

  constructor(
    private esData: ESDataService,
    private datePipe: DatePipe
    ) {}

  ngOnInit() {
    this.esData.getData().subscribe(res => {
      const data = res.data;
      let iter: number = 0;

      for (let index in data) {
        let date = data[index].datetime.split('T').join(' ');
        date = this.datePipe.transform(date, 'yyyy-MM-dd HH:mm');
        
        console.log(date);
        const ports = res.data[index].tcp;
        for (let port in ports) {
          if (this.dateList.length === 0) {
            this.dateList.push(date);
            
            if (!this.storage[port]) {
              this.storage[port] = [];
            }
            this.storage[port][iter] = this.storage[port][iter] || 1;

          } else {
            if (this.dateList.indexOf(date) > - 1) {
              if (!this.storage[port]) {
                this.storage[port] = [];
              }
              this.storage[port][iter] = this.storage[port][iter] + 1 || 1;
            
            } else {
             if (!this.storage[port]) {
                this.storage[port] = [];
             }
             iter += 1;
             this.storage[port][iter] = this.storage[port][iter] + 1 || 1;

            this.dateList.push(date);
            }
            this.portList['80'] = this.storage['80'];
            this.portList['443'] = this.storage['443'];
          }
        }
      }

      this.barChartLabels = this.dateList;
      let test = {
        data: this.portList['80'],
        label: 'Port 80'
      }

      let test2 = {
        data: this.portList['443'],
        label: 'Port 443'
      }
      this.barChartData.pop();
      this.barChartData.push(test);
      this.barChartData.push(test2);
      console.log(this.dateList, this.portList);
    });
  }

  // public countOpenPorts(port:string):void {
  //   if (this.portList.indexOf(port) > ) {

  //   } else {

  //   }
  // }

  public barChartOptions:any = {
    scaleShowVerticalLines: false,
    responsive: true
  };

  public barChartType:string = 'bar';
  public barChartLegend:boolean = true;
 
  // events
  public chartClicked(e:any):void {
    console.log(e);
  }
 
  public chartHovered(e:any):void {
    console.log(e);
  }
 
  public randomize():void {

    // Only Change 3 values
    let data = [
      Math.round(Math.random() * 100),
      59,
      80,
      (Math.random() * 100),
      56,
      (Math.random() * 100),
      40];
    let clone = JSON.parse(JSON.stringify(this.barChartData));
    clone[0].data = data;
    this.barChartData = clone;
    /**
     * (My guess), for Angular to recognize the change in the dataset
     * it has to change the dataset variable directly,
     * so one way around it, is to clone the data, change it and then
     * assign it;
     */
  }
}
