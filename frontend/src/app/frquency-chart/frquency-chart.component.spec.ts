/* tslint:disable:no-unused-variable */
import { async, ComponentFixture, TestBed } from '@angular/core/testing';
import { By } from '@angular/platform-browser';
import { DebugElement } from '@angular/core';

import { FrquencyChartComponent } from './frquency-chart.component';

describe('FrquencyChartComponent', () => {
  let component: FrquencyChartComponent;
  let fixture: ComponentFixture<FrquencyChartComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ FrquencyChartComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(FrquencyChartComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
